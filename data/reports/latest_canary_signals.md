# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T09:52:28.879929+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1116` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0117` n `12`; crypto_alt avg `0.1029` n `232`; crypto_major avg `0.0121` n `8`; equity avg `0.1546` n `130`; fx avg `-0.0004` n `6`; index avg `0.0215` n `26`; metal avg `0.008` n `20`; unknown avg `0.0797` n `792`
- 1h: commodity avg `-0.0199` n `12`; crypto_alt avg `0.0285` n `232`; crypto_major avg `0.1006` n `8`; equity avg `-0.1327` n `130`; fx avg `0.0238` n `6`; index avg `-0.0524` n `26`; metal avg `-0.0518` n `20`; unknown avg `-0.2368` n `790`
- 4h: commodity avg `0.2478` n `12`; crypto_alt avg `-1.5106` n `232`; crypto_major avg `-1.4212` n `8`; equity avg `-1.3747` n `130`; fx avg `0.0482` n `6`; index avg `-0.3096` n `26`; metal avg `-0.689` n `20`; unknown avg `-0.2318` n `770`
- 24h: commodity avg `0.3105` n `12`; crypto_alt avg `0.3502` n `232`; crypto_major avg `-0.0716` n `8`; equity avg `-0.5187` n `130`; fx avg `0.0837` n `6`; index avg `-0.2571` n `26`; metal avg `-0.752` n `20`; unknown avg `0.0207` n `750`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0451`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0337`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0306`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0298`, n `668`, weak_sample_signal
