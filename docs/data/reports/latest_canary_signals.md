# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T14:07:37.861081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1062` n `12`; crypto_alt avg `0.0135` n `234`; crypto_major avg `0.0536` n `8`; equity avg `0.0807` n `140`; fx avg `-0.0078` n `6`; index avg `0.0157` n `26`; metal avg `-0.0936` n `20`; unknown avg `0.7582` n `920`
- 1h: commodity avg `0.2947` n `12`; crypto_alt avg `-0.3957` n `234`; crypto_major avg `0.1245` n `8`; equity avg `1.0115` n `140`; fx avg `-0.0497` n `6`; index avg `0.1328` n `26`; metal avg `-0.0854` n `20`; unknown avg `1.6506` n `898`
- 4h: commodity avg `0.4129` n `12`; crypto_alt avg `0.8128` n `234`; crypto_major avg `0.7949` n `8`; equity avg `0.7755` n `140`; fx avg `0.0098` n `6`; index avg `0.0975` n `26`; metal avg `0.1048` n `20`; unknown avg `1.5711` n `890`
- 24h: commodity avg `-0.111` n `12`; crypto_alt avg `1.7333` n `234`; crypto_major avg `2.3217` n `8`; equity avg `1.7144` n `140`; fx avg `-0.281` n `6`; index avg `0.3528` n `26`; metal avg `-0.0225` n `20`; unknown avg `9050.7447` n `806`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
