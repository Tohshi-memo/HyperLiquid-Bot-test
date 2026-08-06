# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T10:16:21.598968+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0485` n `12`; crypto_alt avg `0.0124` n `230`; crypto_major avg `-0.0419` n `8`; equity avg `-0.0597` n `108`; fx avg `-0.0003` n `6`; index avg `-0.0073` n `25`; metal avg `-0.0214` n `20`; unknown avg `-0.0326` n `782`
- 1h: commodity avg `0.0392` n `12`; crypto_alt avg `-0.1994` n `230`; crypto_major avg `-0.4071` n `8`; equity avg `0.1431` n `108`; fx avg `-0.0085` n `6`; index avg `0.0261` n `25`; metal avg `-0.0606` n `20`; unknown avg `91.6882` n `782`
- 4h: commodity avg `-0.0216` n `12`; crypto_alt avg `-0.3138` n `230`; crypto_major avg `-0.6301` n `8`; equity avg `-0.0092` n `108`; fx avg `0.0118` n `6`; index avg `0.0003` n `25`; metal avg `0.1456` n `20`; unknown avg `91.7385` n `782`
- 24h: commodity avg `-0.2728` n `12`; crypto_alt avg `-0.0736` n `230`; crypto_major avg `-0.5686` n `8`; equity avg `-1.4971` n `108`; fx avg `-0.0309` n `6`; index avg `-0.2989` n `25`; metal avg `0.5111` n `20`; unknown avg `95.8537` n `750`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0751`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
