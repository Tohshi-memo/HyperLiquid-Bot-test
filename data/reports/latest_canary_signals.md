# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T17:07:30.599420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `0.3077` n `233`; crypto_major avg `0.1887` n `8`; equity avg `0.0754` n `135`; fx avg `-0.0024` n `6`; index avg `0.0078` n `26`; metal avg `0.0156` n `20`; unknown avg `0.9219` n `794`
- 1h: commodity avg `0.0258` n `12`; crypto_alt avg `0.3181` n `233`; crypto_major avg `0.2319` n `8`; equity avg `-0.0421` n `135`; fx avg `0.0127` n `6`; index avg `0.0215` n `26`; metal avg `-0.0289` n `20`; unknown avg `0.9632` n `788`
- 4h: commodity avg `0.3252` n `12`; crypto_alt avg `0.2574` n `233`; crypto_major avg `0.0348` n `8`; equity avg `0.5342` n `135`; fx avg `0.0497` n `6`; index avg `-0.0167` n `26`; metal avg `-0.0727` n `20`; unknown avg `-0.1558` n `760`
- 24h: commodity avg `0.9492` n `12`; crypto_alt avg `-4.5031` n `233`; crypto_major avg `-3.6252` n `8`; equity avg `-1.8519` n `135`; fx avg `0.0996` n `6`; index avg `-0.2731` n `26`; metal avg `-1.2644` n `20`; unknown avg `-1.064` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
