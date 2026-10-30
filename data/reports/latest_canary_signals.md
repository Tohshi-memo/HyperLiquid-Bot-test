# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T09:52:28.692193+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1199` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0711` n `13`; crypto_alt avg `0.002` n `238`; crypto_major avg `-0.1003` n `8`; equity avg `-0.3491` n `156`; fx avg `0.0058` n `6`; index avg `-0.0155` n `27`; metal avg `-0.043` n `20`; unknown avg `-0.1367` n `1261`
- 1h: commodity avg `0.0345` n `13`; crypto_alt avg `0.0598` n `238`; crypto_major avg `-0.2238` n `8`; equity avg `-0.4313` n `156`; fx avg `0.0272` n `6`; index avg `-0.0439` n `27`; metal avg `-0.0283` n `20`; unknown avg `14.6956` n `1255`
- 4h: commodity avg `0.1984` n `13`; crypto_alt avg `-0.1896` n `238`; crypto_major avg `-1.1249` n `8`; equity avg `-0.8445` n `156`; fx avg `0.0357` n `6`; index avg `-0.005` n `27`; metal avg `-0.1687` n `20`; unknown avg `4.8369` n `1172`
- 24h: commodity avg `0.1343` n `13`; crypto_alt avg `-3.6076` n `238`; crypto_major avg `-1.1121` n `8`; equity avg `-3.628` n `155`; fx avg `0.1355` n `6`; index avg `-0.4614` n `27`; metal avg `-0.5559` n `20`; unknown avg `31.2484` n `948`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
