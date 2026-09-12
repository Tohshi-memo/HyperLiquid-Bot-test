# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T14:52:25.288306+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0007` n `12`; crypto_alt avg `0.0312` n `233`; crypto_major avg `-0.02` n `8`; equity avg `0.0091` n `136`; fx avg `-0.0023` n `6`; index avg `0.0013` n `26`; metal avg `-0.0021` n `20`; unknown avg `1.0333` n `838`
- 1h: commodity avg `-0.0117` n `12`; crypto_alt avg `0.2986` n `233`; crypto_major avg `0.1459` n `8`; equity avg `0.0155` n `136`; fx avg `0.0014` n `6`; index avg `0.0055` n `26`; metal avg `0.0001` n `20`; unknown avg `1.8985` n `836`
- 4h: commodity avg `-0.0109` n `12`; crypto_alt avg `0.1859` n `233`; crypto_major avg `0.1622` n `8`; equity avg `0.0389` n `136`; fx avg `-0.0006` n `6`; index avg `0.0059` n `26`; metal avg `0.0355` n `20`; unknown avg `2.38` n `824`
- 24h: commodity avg `-0.1386` n `12`; crypto_alt avg `-0.4552` n `233`; crypto_major avg `-1.4335` n `8`; equity avg `-0.2594` n `136`; fx avg `-0.0067` n `6`; index avg `0.0472` n `26`; metal avg `-0.1933` n `20`; unknown avg `10.6234` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
