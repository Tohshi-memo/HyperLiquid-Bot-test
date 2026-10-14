# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T18:07:28.118016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `13`; crypto_alt avg `-0.106` n `236`; crypto_major avg `-0.0746` n `8`; equity avg `0.0616` n `151`; fx avg `-0.0048` n `6`; index avg `0.0162` n `26`; metal avg `0.01` n `20`; unknown avg `0.0256` n `1134`
- 1h: commodity avg `0.0504` n `13`; crypto_alt avg `-0.577` n `236`; crypto_major avg `-0.5776` n `8`; equity avg `-0.5128` n `151`; fx avg `-0.0076` n `6`; index avg `-0.0642` n `26`; metal avg `-0.0258` n `20`; unknown avg `-0.4586` n `1134`
- 4h: commodity avg `0.131` n `13`; crypto_alt avg `-0.1712` n `236`; crypto_major avg `-0.6514` n `8`; equity avg `-1.5571` n `151`; fx avg `-0.0047` n `6`; index avg `-0.2431` n `26`; metal avg `-0.2422` n `20`; unknown avg `-0.0789` n `1101`
- 24h: commodity avg `0.0652` n `13`; crypto_alt avg `-2.5535` n `236`; crypto_major avg `-2.2786` n `8`; equity avg `-3.7973` n `151`; fx avg `-0.1521` n `6`; index avg `-0.5318` n `26`; metal avg `-0.8717` n `20`; unknown avg `1263.0407` n `980`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1005`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0807`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0653`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0594`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0557`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0554`, n `666`, weak_sample_signal
