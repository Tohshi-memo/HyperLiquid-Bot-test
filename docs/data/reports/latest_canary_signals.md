# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T12:07:26.226977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8104` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.6625` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2675` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0147` n `13`; crypto_alt avg `-0.6021` n `239`; crypto_major avg `-0.8615` n `8`; equity avg `-0.5173` n `165`; fx avg `-0.0009` n `6`; index avg `-0.0492` n `27`; metal avg `-0.0902` n `20`; unknown avg `0.9583` n `1246`
- 1h: commodity avg `0.0962` n `13`; crypto_alt avg `-1.1353` n `239`; crypto_major avg `-1.3295` n `8`; equity avg `-0.8991` n `165`; fx avg `0.003` n `6`; index avg `-0.062` n `27`; metal avg `-0.1864` n `20`; unknown avg `200.384` n `1252`
- 4h: commodity avg `-0.0773` n `13`; crypto_alt avg `-1.5204` n `239`; crypto_major avg `-1.815` n `8`; equity avg `-1.5568` n `165`; fx avg `-0.0217` n `6`; index avg `-0.1525` n `27`; metal avg `-0.0046` n `20`; unknown avg `10.4108` n `1236`
- 24h: commodity avg `-0.3068` n `13`; crypto_alt avg `-4.6355` n `239`; crypto_major avg `-4.392` n `8`; equity avg `-8.6274` n `165`; fx avg `-0.0776` n `6`; index avg `-0.8692` n `27`; metal avg `-1.3097` n `20`; unknown avg `13.2402` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0588`, n `668`, weak_sample_signal
