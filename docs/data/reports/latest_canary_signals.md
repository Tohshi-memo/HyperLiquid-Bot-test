# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T16:37:27.416136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `0.0156` n `230`; crypto_major avg `-0.0103` n `8`; equity avg `-0.0511` n `108`; fx avg `-0.0032` n `6`; index avg `-0.0039` n `25`; metal avg `0.0663` n `20`; unknown avg `-0.0515` n `782`
- 1h: commodity avg `0.202` n `12`; crypto_alt avg `0.0794` n `230`; crypto_major avg `0.1774` n `8`; equity avg `-0.0246` n `108`; fx avg `0.0122` n `6`; index avg `-0.0312` n `25`; metal avg `-0.0872` n `20`; unknown avg `-0.0702` n `782`
- 4h: commodity avg `-0.1289` n `12`; crypto_alt avg `-0.0266` n `230`; crypto_major avg `0.2535` n `8`; equity avg `-0.1814` n `108`; fx avg `-0.0093` n `6`; index avg `-0.0852` n `25`; metal avg `0.1346` n `20`; unknown avg `-0.1107` n `782`
- 24h: commodity avg `0.0361` n `12`; crypto_alt avg `0.9142` n `230`; crypto_major avg `1.0299` n `8`; equity avg `0.2406` n `108`; fx avg `0.0116` n `6`; index avg `0.0833` n `25`; metal avg `0.6492` n `20`; unknown avg `0.8242` n `749`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
