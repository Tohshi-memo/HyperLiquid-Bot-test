# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T17:07:32.536630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0887` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0241` n `13`; crypto_alt avg `-0.2729` n `236`; crypto_major avg `-0.1497` n `8`; equity avg `-0.3635` n `151`; fx avg `-0.0035` n `6`; index avg `-0.0668` n `26`; metal avg `-0.0324` n `20`; unknown avg `-0.2973` n `1175`
- 1h: commodity avg `0.372` n `13`; crypto_alt avg `-0.8315` n `236`; crypto_major avg `-0.2605` n `8`; equity avg `-0.5298` n `151`; fx avg `0.0049` n `6`; index avg `-0.1167` n `26`; metal avg `-0.0766` n `20`; unknown avg `-0.6286` n `1172`
- 4h: commodity avg `0.459` n `13`; crypto_alt avg `-1.9355` n `236`; crypto_major avg `-1.5289` n `8`; equity avg `-2.5453` n `151`; fx avg `0.0082` n `6`; index avg `-0.4402` n `26`; metal avg `-0.1733` n `20`; unknown avg `0.9985` n `996`
- 24h: commodity avg `0.1809` n `13`; crypto_alt avg `-1.3317` n `236`; crypto_major avg `-1.3912` n `8`; equity avg `-1.9663` n `151`; fx avg `0.0054` n `6`; index avg `-0.3889` n `26`; metal avg `0.0433` n `20`; unknown avg `-0.4087` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1288`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0927`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0901`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0846`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0777`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0717`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
