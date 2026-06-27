# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T20:22:27.737534+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3262` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `0.1039` n `228`; crypto_major avg `0.0762` n `8`; equity avg `0.0193` n `88`; fx avg `0.0033` n `6`; index avg `0.0146` n `23`; metal avg `0.005` n `20`; unknown avg `-0.0304` n `764`
- 1h: commodity avg `0.0573` n `12`; crypto_alt avg `-0.3095` n `228`; crypto_major avg `-0.3632` n `8`; equity avg `-0.0633` n `88`; fx avg `0.005` n `6`; index avg `0.015` n `23`; metal avg `-0.0165` n `20`; unknown avg `-0.029` n `764`
- 4h: commodity avg `0.0417` n `12`; crypto_alt avg `-1.1658` n `228`; crypto_major avg `-1.3507` n `8`; equity avg `-0.1462` n `88`; fx avg `-0.001` n `6`; index avg `-0.0245` n `23`; metal avg `-0.0568` n `20`; unknown avg `0.2288` n `764`
- 24h: commodity avg `0.2429` n `12`; crypto_alt avg `-0.612` n `228`; crypto_major avg `-0.6829` n `8`; equity avg `0.4243` n `88`; fx avg `0.0887` n `6`; index avg `0.0153` n `23`; metal avg `0.1068` n `20`; unknown avg `-0.2546` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2082`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
