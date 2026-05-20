# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T17:09:31.131755+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.4009` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0819` n `12`; crypto_alt avg `-0.0245` n `228`; crypto_major avg `-0.0525` n `8`; equity avg `-0.0629` n `66`; fx avg `-0.0035` n `6`; index avg `-0.0169` n `23`; metal avg `0.0886` n `18`; unknown avg `0.4027` n `384`
- 1h: commodity avg `-0.3326` n `12`; crypto_alt avg `-0.199` n `228`; crypto_major avg `-0.1755` n `8`; equity avg `-0.2199` n `66`; fx avg `-0.0046` n `6`; index avg `-0.093` n `23`; metal avg `-0.0361` n `18`; unknown avg `1.5032` n `384`
- 4h: commodity avg `-1.6786` n `12`; crypto_alt avg `1.0737` n `228`; crypto_major avg `0.7223` n `8`; equity avg `0.4532` n `66`; fx avg `-0.0011` n `6`; index avg `0.6278` n `23`; metal avg `0.8319` n `18`; unknown avg `0.8989` n `384`
- 24h: commodity avg `-2.6829` n `12`; crypto_alt avg `2.1619` n `228`; crypto_major avg `1.381` n `8`; equity avg `0.9392` n `66`; fx avg `-0.0293` n `6`; index avg `0.6859` n `23`; metal avg `0.9658` n `18`; unknown avg `2.5076` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.043`, n `668`, weak_sample_signal
