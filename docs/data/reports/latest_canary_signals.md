# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T14:52:45.447857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.7087` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.2634` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0711` n `12`; crypto_alt avg `-0.057` n `229`; crypto_major avg `-0.0029` n `8`; equity avg `-0.0301` n `88`; fx avg `-0.0057` n `6`; index avg `-0.0099` n `25`; metal avg `-0.1068` n `20`; unknown avg `-0.1747` n `765`
- 1h: commodity avg `0.0452` n `12`; crypto_alt avg `0.2421` n `229`; crypto_major avg `0.0033` n `8`; equity avg `0.1744` n `88`; fx avg `0.0026` n `6`; index avg `0.0275` n `25`; metal avg `-0.1538` n `20`; unknown avg `-0.0808` n `765`
- 4h: commodity avg `0.1716` n `12`; crypto_alt avg `-0.47` n `229`; crypto_major avg `-1.1557` n `8`; equity avg `0.553` n `88`; fx avg `0.0308` n `6`; index avg `0.1077` n `25`; metal avg `-0.2925` n `20`; unknown avg `-0.3175` n `765`
- 24h: commodity avg `-0.0083` n `12`; crypto_alt avg `-0.491` n `229`; crypto_major avg `-1.0023` n `8`; equity avg `-0.1354` n `88`; fx avg `0.1743` n `6`; index avg `0.0557` n `25`; metal avg `-0.4392` n `20`; unknown avg `0.4357` n `661`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0554`, n `668`, weak_sample_signal
