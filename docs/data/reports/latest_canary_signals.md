# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T10:07:27.422393+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0445` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0433` n `12`; crypto_alt avg `0.0477` n `230`; crypto_major avg `0.0983` n `8`; equity avg `-0.0184` n `94`; fx avg `-0.0077` n `6`; index avg `-0.0096` n `25`; metal avg `-0.0429` n `20`; unknown avg `0.0178` n `768`
- 1h: commodity avg `0.165` n `12`; crypto_alt avg `0.0638` n `230`; crypto_major avg `0.1487` n `8`; equity avg `-0.1623` n `94`; fx avg `-0.0257` n `6`; index avg `-0.0558` n `25`; metal avg `-0.0435` n `20`; unknown avg `-0.0063` n `768`
- 4h: commodity avg `0.0173` n `12`; crypto_alt avg `-0.9138` n `230`; crypto_major avg `-1.0927` n `8`; equity avg `-0.6144` n `94`; fx avg `-0.0859` n `6`; index avg `-0.0482` n `25`; metal avg `-0.1331` n `20`; unknown avg `-0.0822` n `762`
- 24h: commodity avg `-0.1549` n `12`; crypto_alt avg `-0.8003` n `230`; crypto_major avg `-0.8434` n `8`; equity avg `-2.8598` n `93`; fx avg `0.0297` n `6`; index avg `-0.4765` n `25`; metal avg `-0.0116` n `20`; unknown avg `-0.0569` n `745`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
