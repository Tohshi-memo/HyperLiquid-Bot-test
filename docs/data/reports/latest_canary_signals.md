# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-16T04:07:26.659635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `12`; crypto_alt avg `-0.0635` n `230`; crypto_major avg `-0.0228` n `8`; equity avg `0.0097` n `114`; fx avg `0.0014` n `6`; index avg `0.0015` n `25`; metal avg `-0.0021` n `20`; unknown avg `0.0593` n `791`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `-0.0935` n `230`; crypto_major avg `-0.0714` n `8`; equity avg `0.0972` n `114`; fx avg `-0.0035` n `6`; index avg `0.0073` n `25`; metal avg `0.0011` n `20`; unknown avg `0.0261` n `791`
- 4h: commodity avg `0.0689` n `12`; crypto_alt avg `-0.1637` n `230`; crypto_major avg `0.1115` n `8`; equity avg `0.1439` n `114`; fx avg `0.0019` n `6`; index avg `0.0096` n `25`; metal avg `0.0172` n `20`; unknown avg `-0.0148` n `791`
- 24h: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.0294` n `230`; crypto_major avg `-0.0787` n `8`; equity avg `0.2315` n `114`; fx avg `-0.0185` n `6`; index avg `0.0162` n `25`; metal avg `0.0167` n `20`; unknown avg `-0.0526` n `759`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2214`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1848`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1706`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1449`, n `668`, weak_sample_signal
