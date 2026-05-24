# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T21:37:17.152095+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1959` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.03` n `12`; crypto_alt avg `-1.0868` n `228`; crypto_major avg `-0.733` n `8`; equity avg `-0.1913` n `67`; fx avg `-0.0109` n `6`; index avg `0.0081` n `23`; metal avg `-0.11` n `18`; unknown avg `0.4844` n `396`
- 1h: commodity avg `-0.0139` n `12`; crypto_alt avg `-1.1769` n `228`; crypto_major avg `-0.8138` n `8`; equity avg `-0.1875` n `67`; fx avg `-0.0043` n `6`; index avg `-0.0919` n `23`; metal avg `-0.2542` n `18`; unknown avg `-0.0133` n `396`
- 4h: commodity avg `0.0746` n `12`; crypto_alt avg `-1.7236` n `228`; crypto_major avg `-1.2188` n `8`; equity avg `-0.0813` n `67`; fx avg `0.042` n `6`; index avg `-0.0229` n `23`; metal avg `-0.3873` n `18`; unknown avg `-0.5036` n `396`
- 24h: commodity avg `1.288` n `12`; crypto_alt avg `-3.3719` n `228`; crypto_major avg `-0.768` n `8`; equity avg `0.3003` n `67`; fx avg `0.1115` n `6`; index avg `-0.0832` n `23`; metal avg `-0.3448` n `18`; unknown avg `-0.3083` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
