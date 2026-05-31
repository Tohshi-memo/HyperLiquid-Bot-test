# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T16:37:23.402568+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.252` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0813` n `12`; crypto_alt avg `-0.4785` n `228`; crypto_major avg `-0.5723` n `8`; equity avg `-0.0574` n `69`; fx avg `0.0043` n `6`; index avg `-0.0321` n `23`; metal avg `0.0023` n `18`; unknown avg `1.0988` n `421`
- 1h: commodity avg `-0.0666` n `12`; crypto_alt avg `-0.9231` n `228`; crypto_major avg `-0.8443` n `8`; equity avg `-0.0739` n `69`; fx avg `-0.0084` n `6`; index avg `0.0193` n `23`; metal avg `-0.0349` n `18`; unknown avg `0.6824` n `421`
- 4h: commodity avg `0.0636` n `12`; crypto_alt avg `-1.6718` n `228`; crypto_major avg `-1.1119` n `8`; equity avg `-0.0502` n `69`; fx avg `-0.0167` n `6`; index avg `0.1401` n `23`; metal avg `-0.085` n `18`; unknown avg `0.5087` n `421`
- 24h: commodity avg `0.5401` n `12`; crypto_alt avg `-1.6863` n `228`; crypto_major avg `-0.779` n `8`; equity avg `0.889` n `69`; fx avg `-0.0226` n `6`; index avg `-0.0173` n `23`; metal avg `-0.1449` n `18`; unknown avg `-0.0033` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
