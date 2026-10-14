# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T14:22:28.116901+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5226` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0503` n `13`; crypto_alt avg `-0.3157` n `235`; crypto_major avg `-0.3848` n `8`; equity avg `-0.0522` n `151`; fx avg `0.0019` n `6`; index avg `0.0067` n `26`; metal avg `-0.018` n `20`; unknown avg `0.0378` n `1112`
- 1h: commodity avg `-0.0594` n `13`; crypto_alt avg `-0.344` n `235`; crypto_major avg `-0.5728` n `8`; equity avg `-0.5461` n `151`; fx avg `-0.0336` n `6`; index avg `-0.0162` n `26`; metal avg `-0.0883` n `20`; unknown avg `0.5936` n `1108`
- 4h: commodity avg `-0.2764` n `13`; crypto_alt avg `-1.987` n `235`; crypto_major avg `-1.7939` n `8`; equity avg `-2.0455` n `151`; fx avg `-0.1124` n `6`; index avg `-0.2713` n `26`; metal avg `-0.5827` n `20`; unknown avg `2.9463` n `1101`
- 24h: commodity avg `0.2438` n `13`; crypto_alt avg `-2.9208` n `235`; crypto_major avg `-2.3175` n `8`; equity avg `-2.2285` n `151`; fx avg `-0.1437` n `6`; index avg `-0.2448` n `26`; metal avg `-0.7344` n `20`; unknown avg `1262.6044` n `981`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1192`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.111`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.096`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0749`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0582`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
