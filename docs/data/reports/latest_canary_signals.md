# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T01:36:18.366415+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5972` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.5137` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0254` n `13`; crypto_alt avg `0.1167` n `235`; crypto_major avg `0.1303` n `8`; equity avg `-0.1274` n `151`; fx avg `0.0205` n `6`; index avg `-0.0257` n `26`; metal avg `-0.0679` n `20`; unknown avg `-0.0178` n `1135`
- 1h: commodity avg `-0.0014` n `13`; crypto_alt avg `0.5074` n `235`; crypto_major avg `0.7752` n `8`; equity avg `-0.475` n `151`; fx avg `0.0816` n `6`; index avg `-0.1163` n `26`; metal avg `-0.0641` n `20`; unknown avg `1.0419` n `1133`
- 4h: commodity avg `0.0159` n `13`; crypto_alt avg `-2.5689` n `235`; crypto_major avg `-1.7743` n `8`; equity avg `-1.3939` n `151`; fx avg `0.0673` n `6`; index avg `-0.2606` n `26`; metal avg `-0.1771` n `20`; unknown avg `4.7115` n `1111`
- 24h: commodity avg `0.7198` n `13`; crypto_alt avg `-5.3282` n `235`; crypto_major avg `-3.5703` n `8`; equity avg `-4.7223` n `151`; fx avg `-0.0676` n `6`; index avg `-0.5745` n `26`; metal avg `-0.3718` n `20`; unknown avg `0.5855` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2089`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1883`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1202`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.104`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1011`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0832`, n `666`, weak_sample_signal
