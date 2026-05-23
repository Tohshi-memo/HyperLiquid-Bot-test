# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T22:52:14.122650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5866` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `0.2278` n `228`; crypto_major avg `0.2816` n `8`; equity avg `0.0886` n `67`; fx avg `-0.0007` n `6`; index avg `-0.0099` n `23`; metal avg `0.0739` n `18`; unknown avg `0.042` n `396`
- 1h: commodity avg `-0.2262` n `12`; crypto_alt avg `-0.3901` n `228`; crypto_major avg `-0.0692` n `8`; equity avg `0.0857` n `67`; fx avg `0.0395` n `6`; index avg `-0.161` n `23`; metal avg `0.1099` n `18`; unknown avg `0.0752` n `396`
- 4h: commodity avg `-1.9344` n `12`; crypto_alt avg `0.6271` n `228`; crypto_major avg `0.6522` n `8`; equity avg `0.773` n `67`; fx avg `0.0687` n `6`; index avg `0.1698` n `23`; metal avg `0.4776` n `18`; unknown avg `0.1817` n `396`
- 24h: commodity avg `-2.7452` n `12`; crypto_alt avg `1.6056` n `228`; crypto_major avg `1.2915` n `8`; equity avg `1.5111` n `67`; fx avg `0.0509` n `6`; index avg `0.5082` n `23`; metal avg `0.6611` n `18`; unknown avg `-0.2307` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
