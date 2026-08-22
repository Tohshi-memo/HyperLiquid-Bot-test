# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T10:52:24.561559+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.0461` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.9864` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7513` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0029` n `12`; crypto_alt avg `-0.3255` n `230`; crypto_major avg `-0.4005` n `8`; equity avg `-0.0211` n `121`; fx avg `0.0018` n `6`; index avg `-0.002` n `25`; metal avg `-0.0124` n `20`; unknown avg `-0.0951` n `794`
- 1h: commodity avg `-0.0047` n `12`; crypto_alt avg `-0.6893` n `230`; crypto_major avg `-0.5421` n `8`; equity avg `-0.0689` n `121`; fx avg `0.0175` n `6`; index avg `-0.0104` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.1049` n `794`
- 4h: commodity avg `-0.0357` n `12`; crypto_alt avg `-2.0118` n `230`; crypto_major avg `-2.0218` n `8`; equity avg `-0.2705` n `121`; fx avg `0.0111` n `6`; index avg `-0.0354` n `25`; metal avg `0.0243` n `20`; unknown avg `0.6548` n `794`
- 24h: commodity avg `-0.0412` n `12`; crypto_alt avg `1.3291` n `230`; crypto_major avg `2.4348` n `8`; equity avg `-1.0544` n `121`; fx avg `0.0496` n `6`; index avg `-0.114` n `25`; metal avg `-0.1137` n `20`; unknown avg `1.4323` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
