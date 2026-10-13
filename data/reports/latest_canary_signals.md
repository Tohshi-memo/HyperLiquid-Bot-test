# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T08:22:28.120443+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `-0.0306` n `235`; crypto_major avg `0.0045` n `8`; equity avg `0.1371` n `151`; fx avg `-0.0117` n `6`; index avg `0.0154` n `26`; metal avg `0.0239` n `20`; unknown avg `1.6383` n `1135`
- 1h: commodity avg `-0.0438` n `13`; crypto_alt avg `-0.0685` n `235`; crypto_major avg `0.219` n `8`; equity avg `0.4133` n `151`; fx avg `0.0095` n `6`; index avg `0.0438` n `26`; metal avg `-0.0136` n `20`; unknown avg `0.5288` n `1117`
- 4h: commodity avg `-0.0164` n `13`; crypto_alt avg `0.6803` n `235`; crypto_major avg `0.6917` n `8`; equity avg `0.356` n `151`; fx avg `0.026` n `6`; index avg `0.1034` n `26`; metal avg `0.0755` n `20`; unknown avg `1.2246` n `1097`
- 24h: commodity avg `0.2363` n `13`; crypto_alt avg `-3.436` n `235`; crypto_major avg `-1.6373` n `8`; equity avg `-3.0128` n `151`; fx avg `0.0739` n `6`; index avg `-0.4198` n `26`; metal avg `0.0751` n `20`; unknown avg `0.354` n `883`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1905`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1712`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1534`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1326`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0878`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0765`, n `666`, weak_sample_signal
