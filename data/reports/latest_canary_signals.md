# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T10:07:30.786159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2164` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0301` n `13`; crypto_alt avg `0.1126` n `238`; crypto_major avg `-0.1057` n `8`; equity avg `-0.0039` n `156`; fx avg `0.0166` n `6`; index avg `-0.0202` n `27`; metal avg `-0.03` n `20`; unknown avg `0.0133` n `1255`
- 1h: commodity avg `0.1202` n `13`; crypto_alt avg `0.0501` n `238`; crypto_major avg `-0.3406` n `8`; equity avg `-0.5725` n `156`; fx avg `0.0244` n `6`; index avg `-0.0968` n `27`; metal avg `-0.0665` n `20`; unknown avg `-0.1283` n `1255`
- 4h: commodity avg `0.278` n `13`; crypto_alt avg `0.0936` n `238`; crypto_major avg `-1.2357` n `8`; equity avg `-0.755` n `156`; fx avg `0.0413` n `6`; index avg `-0.0193` n `27`; metal avg `-0.0977` n `20`; unknown avg `5.4681` n `1190`
- 24h: commodity avg `0.2546` n `13`; crypto_alt avg `-3.5302` n `238`; crypto_major avg `-1.123` n `8`; equity avg `-3.7459` n `155`; fx avg `0.1413` n `6`; index avg `-0.4676` n `27`; metal avg `-0.6238` n `20`; unknown avg `31.7818` n `962`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
