# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T16:07:33.156323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.5734` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4021` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1151` n `13`; crypto_alt avg `-0.0162` n `236`; crypto_major avg `-0.1058` n `8`; equity avg `-0.2581` n `151`; fx avg `-0.0118` n `6`; index avg `-0.0651` n `26`; metal avg `-0.0473` n `20`; unknown avg `0.0808` n `1164`
- 1h: commodity avg `0.2906` n `13`; crypto_alt avg `-0.213` n `236`; crypto_major avg `-0.4326` n `8`; equity avg `-0.3895` n `151`; fx avg `-0.0417` n `6`; index avg `-0.1088` n `26`; metal avg `-0.1778` n `20`; unknown avg `0.0981` n `1134`
- 4h: commodity avg `-0.1317` n `13`; crypto_alt avg `-1.6574` n `236`; crypto_major avg `-1.7551` n `8`; equity avg `-2.3482` n `151`; fx avg `-0.0172` n `6`; index avg `-0.353` n `26`; metal avg `-0.1817` n `20`; unknown avg `1.3738` n `996`
- 24h: commodity avg `-0.2521` n `13`; crypto_alt avg `-0.884` n `236`; crypto_major avg `-1.5078` n `8`; equity avg `-1.4801` n `151`; fx avg `0.014` n `6`; index avg `-0.2718` n `26`; metal avg `0.0772` n `20`; unknown avg `0.1309` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1186`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0958`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0933`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0792`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.079`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0771`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0766`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
