# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T19:22:31.577184+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.025` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0764` n `13`; crypto_alt avg `-0.1827` n `239`; crypto_major avg `-0.0382` n `8`; equity avg `-0.227` n `158`; fx avg `0.0068` n `6`; index avg `-0.035` n `27`; metal avg `0.0134` n `20`; unknown avg `0.114` n `1264`
- 1h: commodity avg `-0.3119` n `13`; crypto_alt avg `-0.3127` n `239`; crypto_major avg `-0.3905` n `8`; equity avg `-0.1718` n `158`; fx avg `-0.0116` n `6`; index avg `-0.0386` n `27`; metal avg `-0.0145` n `20`; unknown avg `0.7542` n `1258`
- 4h: commodity avg `-1.3035` n `13`; crypto_alt avg `-1.5976` n `239`; crypto_major avg `-1.0759` n `8`; equity avg `-1.3278` n `158`; fx avg `-0.0387` n `6`; index avg `-0.0509` n `27`; metal avg `0.2785` n `20`; unknown avg `4.0286` n `1252`
- 24h: commodity avg `-1.7851` n `13`; crypto_alt avg `1.5827` n `239`; crypto_major avg `2.077` n `8`; equity avg `-0.7494` n `158`; fx avg `0.0331` n `6`; index avg `0.1235` n `27`; metal avg `1.274` n `20`; unknown avg `0.7811` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2684`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1274`, n `668`, weak_sample_signal
