# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T20:52:28.248396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.7625` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-1.735` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.6991` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0167` n `13`; crypto_alt avg `-0.217` n `235`; crypto_major avg `-0.0842` n `8`; equity avg `-0.0398` n `143`; fx avg `-0.0066` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0419` n `20`; unknown avg `-0.2451` n `984`
- 1h: commodity avg `0.0259` n `13`; crypto_alt avg `0.1872` n `235`; crypto_major avg `0.0658` n `8`; equity avg `-0.0017` n `143`; fx avg `-0.0204` n `6`; index avg `0.0009` n `26`; metal avg `-0.0589` n `20`; unknown avg `20.5806` n `924`
- 4h: commodity avg `0.2996` n `13`; crypto_alt avg `-3.0986` n `235`; crypto_major avg `-1.6884` n `8`; equity avg `0.0466` n `143`; fx avg `-0.027` n `6`; index avg `0.0107` n `26`; metal avg `0.0741` n `20`; unknown avg `4.2678` n `924`
- 24h: commodity avg `0.0265` n `13`; crypto_alt avg `-1.8538` n `235`; crypto_major avg `-1.089` n `8`; equity avg `0.7008` n `142`; fx avg `-0.1474` n `6`; index avg `0.2932` n `26`; metal avg `-0.2747` n `20`; unknown avg `0.0367` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
