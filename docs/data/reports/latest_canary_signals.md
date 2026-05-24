# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T08:07:19.836489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0385` n `12`; crypto_alt avg `-0.1389` n `228`; crypto_major avg `-0.0665` n `8`; equity avg `-0.0086` n `67`; fx avg `-0.0004` n `6`; index avg `-0.0593` n `23`; metal avg `0.0209` n `18`; unknown avg `-0.1035` n `396`
- 1h: commodity avg `0.1375` n `12`; crypto_alt avg `-0.3483` n `228`; crypto_major avg `-0.2193` n `8`; equity avg `-0.0175` n `67`; fx avg `0.0031` n `6`; index avg `-0.0537` n `23`; metal avg `0.0554` n `18`; unknown avg `-0.0581` n `396`
- 4h: commodity avg `0.1471` n `12`; crypto_alt avg `-0.2269` n `228`; crypto_major avg `0.2506` n `8`; equity avg `0.2128` n `67`; fx avg `0.0131` n `6`; index avg `-0.0011` n `23`; metal avg `0.0568` n `18`; unknown avg `0.0393` n `386`
- 24h: commodity avg `-2.7567` n `12`; crypto_alt avg `4.3297` n `228`; crypto_major avg `4.2965` n `8`; equity avg `2.8183` n `67`; fx avg `0.0568` n `6`; index avg `1.3649` n `23`; metal avg `1.34` n `18`; unknown avg `1.8938` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
