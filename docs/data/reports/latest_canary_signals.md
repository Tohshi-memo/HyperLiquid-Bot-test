# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-12T14:22:25.006723+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7753` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.4458` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.2939` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0483` n `13`; crypto_alt avg `-0.4832` n `239`; crypto_major avg `-0.6246` n `8`; equity avg `-0.3084` n `162`; fx avg `0.0066` n `6`; index avg `-0.0271` n `27`; metal avg `0.074` n `20`; unknown avg `-0.2017` n `1261`
- 1h: commodity avg `-0.1302` n `13`; crypto_alt avg `-0.4985` n `239`; crypto_major avg `-0.8666` n `8`; equity avg `-0.8377` n `162`; fx avg `0.0014` n `6`; index avg `-0.0317` n `27`; metal avg `-0.0805` n `20`; unknown avg `2.6408` n `1255`
- 4h: commodity avg `0.1896` n `13`; crypto_alt avg `-1.9789` n `239`; crypto_major avg `-2.5857` n `8`; equity avg `-2.3682` n `162`; fx avg `-0.0006` n `6`; index avg `-0.1399` n `27`; metal avg `-0.2918` n `20`; unknown avg `19.6385` n `1247`
- 24h: commodity avg `0.0161` n `13`; crypto_alt avg `-3.7077` n `239`; crypto_major avg `-3.1818` n `8`; equity avg `-3.1374` n `162`; fx avg `-0.0572` n `6`; index avg `-0.1652` n `27`; metal avg `-0.997` n `20`; unknown avg `0.9586` n `1138`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
