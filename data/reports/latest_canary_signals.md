# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T22:22:34.152916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0109` n `13`; crypto_alt avg `-0.5184` n `235`; crypto_major avg `-0.2924` n `8`; equity avg `-0.0098` n `151`; fx avg `0.0019` n `6`; index avg `-0.0169` n `26`; metal avg `-0.0068` n `20`; unknown avg `-0.0206` n `1135`
- 1h: commodity avg `0.0653` n `13`; crypto_alt avg `-1.2025` n `235`; crypto_major avg `-0.8029` n `8`; equity avg `-0.0556` n `151`; fx avg `0.0125` n `6`; index avg `-0.0094` n `26`; metal avg `0.0085` n `20`; unknown avg `0.7088` n `1095`
- 4h: commodity avg `-0.1864` n `13`; crypto_alt avg `-1.1209` n `235`; crypto_major avg `-0.5536` n `8`; equity avg `0.014` n `151`; fx avg `-0.0049` n `6`; index avg `0.0057` n `26`; metal avg `0.0487` n `20`; unknown avg `0.6529` n `1060`
- 24h: commodity avg `0.2732` n `13`; crypto_alt avg `-3.969` n `235`; crypto_major avg `-2.4025` n `8`; equity avg `-3.4357` n `151`; fx avg `-0.1422` n `6`; index avg `-0.3433` n `26`; metal avg `-0.0514` n `20`; unknown avg `0.0707` n `853`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2038`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1744`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1185`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1016`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0895`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0865`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0757`, n `666`, weak_sample_signal
