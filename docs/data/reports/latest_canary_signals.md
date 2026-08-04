# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T00:07:31.464132+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0688` n `12`; crypto_alt avg `0.1222` n `230`; crypto_major avg `0.078` n `8`; equity avg `-0.0396` n `107`; fx avg `0.0055` n `6`; index avg `-0.0028` n `25`; metal avg `0.0671` n `20`; unknown avg `-0.023` n `780`
- 1h: commodity avg `0.0838` n `12`; crypto_alt avg `0.1005` n `230`; crypto_major avg `0.0866` n `8`; equity avg `0.1709` n `107`; fx avg `0.0425` n `6`; index avg `0.061` n `25`; metal avg `0.0853` n `20`; unknown avg `-0.1267` n `780`
- 4h: commodity avg `0.1212` n `12`; crypto_alt avg `-0.0325` n `230`; crypto_major avg `-0.3889` n `8`; equity avg `0.5257` n `107`; fx avg `0.0764` n `6`; index avg `0.1199` n `25`; metal avg `0.1176` n `20`; unknown avg `-0.0` n `780`
- 24h: commodity avg `0.0602` n `12`; crypto_alt avg `0.4107` n `230`; crypto_major avg `0.1739` n `8`; equity avg `2.4757` n `107`; fx avg `-0.1828` n `6`; index avg `0.2496` n `25`; metal avg `-0.1746` n `20`; unknown avg `0.0831` n `763`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
