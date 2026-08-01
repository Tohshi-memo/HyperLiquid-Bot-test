# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T06:52:33.671034+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `12`; crypto_alt avg `0.0337` n `230`; crypto_major avg `0.0353` n `8`; equity avg `-0.0364` n `102`; fx avg `-0.0023` n `6`; index avg `0.0116` n `25`; metal avg `0.0039` n `20`; unknown avg `0.0145` n `781`
- 1h: commodity avg `-0.0125` n `12`; crypto_alt avg `0.1802` n `230`; crypto_major avg `0.1787` n `8`; equity avg `0.0677` n `102`; fx avg `0.005` n `6`; index avg `0.0383` n `25`; metal avg `-0.0017` n `20`; unknown avg `0.0393` n `765`
- 4h: commodity avg `-0.0301` n `12`; crypto_alt avg `0.023` n `230`; crypto_major avg `-0.0826` n `8`; equity avg `-0.026` n `102`; fx avg `0.0243` n `6`; index avg `-0.0102` n `25`; metal avg `-0.0071` n `20`; unknown avg `-0.0554` n `765`
- 24h: commodity avg `0.8365` n `12`; crypto_alt avg `0.1733` n `230`; crypto_major avg `-1.6572` n `8`; equity avg `-2.1142` n `102`; fx avg `0.01` n `6`; index avg `-0.2299` n `25`; metal avg `-0.1992` n `20`; unknown avg `4.6855` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
