# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T18:07:35.561610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0101` n `12`; crypto_alt avg `0.0535` n `231`; crypto_major avg `0.1347` n `8`; equity avg `-0.0468` n `122`; fx avg `0.0019` n `6`; index avg `-0.0045` n `25`; metal avg `0.0077` n `20`; unknown avg `0.0073` n `795`
- 1h: commodity avg `-0.0109` n `12`; crypto_alt avg `0.1102` n `231`; crypto_major avg `0.3831` n `8`; equity avg `-0.0476` n `122`; fx avg `0.0092` n `6`; index avg `-0.0164` n `25`; metal avg `0.0397` n `20`; unknown avg `-0.0037` n `795`
- 4h: commodity avg `0.0448` n `12`; crypto_alt avg `0.1223` n `231`; crypto_major avg `0.5835` n `8`; equity avg `0.1075` n `122`; fx avg `-0.0195` n `6`; index avg `-0.017` n `25`; metal avg `0.2323` n `20`; unknown avg `-0.0856` n `795`
- 24h: commodity avg `-0.5806` n `12`; crypto_alt avg `-0.6714` n `231`; crypto_major avg `0.8185` n `8`; equity avg `1.3909` n `122`; fx avg `0.056` n `6`; index avg `0.1582` n `25`; metal avg `-0.0068` n `20`; unknown avg `-0.6762` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
