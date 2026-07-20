# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T07:07:33.783853+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0402` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0717` n `12`; crypto_alt avg `0.0122` n `230`; crypto_major avg `0.0949` n `8`; equity avg `0.0231` n `98`; fx avg `0.0133` n `6`; index avg `0.0163` n `25`; metal avg `-0.0054` n `20`; unknown avg `0.0733` n `769`
- 1h: commodity avg `-0.0107` n `12`; crypto_alt avg `0.1163` n `230`; crypto_major avg `-0.2281` n `8`; equity avg `-0.0581` n `98`; fx avg `0.0258` n `6`; index avg `0.0006` n `25`; metal avg `-0.0181` n `20`; unknown avg `0.0241` n `769`
- 4h: commodity avg `0.1189` n `12`; crypto_alt avg `-0.8487` n `230`; crypto_major avg `-1.0574` n `8`; equity avg `-0.2123` n `98`; fx avg `-0.0167` n `6`; index avg `-0.0172` n `25`; metal avg `-0.1535` n `20`; unknown avg `-0.2855` n `753`
- 24h: commodity avg `0.0039` n `12`; crypto_alt avg `-0.6388` n `230`; crypto_major avg `-0.8222` n `8`; equity avg `-0.1367` n `97`; fx avg `-0.0276` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0594` n `20`; unknown avg `-0.1103` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.104`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0981`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0914`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0891`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0859`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
