# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T02:52:24.716045+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2156` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1378` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0172` n `12`; crypto_alt avg `-0.4198` n `231`; crypto_major avg `-0.4321` n `8`; equity avg `-0.074` n `127`; fx avg `-0.0091` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.1092` n `792`
- 1h: commodity avg `0.0655` n `12`; crypto_alt avg `-1.8962` n `231`; crypto_major avg `-1.1306` n `8`; equity avg `-0.1753` n `127`; fx avg `0.0211` n `6`; index avg `0.0072` n `26`; metal avg `0.0776` n `20`; unknown avg `0.488` n `792`
- 4h: commodity avg `-0.0099` n `12`; crypto_alt avg `-1.5662` n `231`; crypto_major avg `-1.1631` n `8`; equity avg `-0.01` n `127`; fx avg `-0.0319` n `6`; index avg `0.0525` n `26`; metal avg `-0.1305` n `20`; unknown avg `0.0153` n `792`
- 24h: commodity avg `0.3796` n `12`; crypto_alt avg `0.2376` n `231`; crypto_major avg `1.5347` n `8`; equity avg `-0.1258` n `127`; fx avg `-0.0111` n `6`; index avg `0.0127` n `26`; metal avg `-0.1286` n `20`; unknown avg `0.566` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.06`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
