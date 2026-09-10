# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T12:07:33.731259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2418` n `12`; crypto_alt avg `-0.228` n `233`; crypto_major avg `-0.1359` n `8`; equity avg `-0.2337` n `134`; fx avg `0.0047` n `6`; index avg `-0.0515` n `26`; metal avg `-0.0355` n `20`; unknown avg `-0.1006` n `795`
- 1h: commodity avg `0.3032` n `12`; crypto_alt avg `-0.0469` n `233`; crypto_major avg `0.0005` n `8`; equity avg `-0.3589` n `134`; fx avg `-0.0085` n `6`; index avg `-0.0806` n `26`; metal avg `-0.1026` n `20`; unknown avg `-0.2538` n `795`
- 4h: commodity avg `0.4447` n `12`; crypto_alt avg `-0.3236` n `233`; crypto_major avg `-0.3975` n `8`; equity avg `-0.7636` n `134`; fx avg `0.0363` n `6`; index avg `-0.174` n `26`; metal avg `-0.6349` n `20`; unknown avg `0.0026` n `789`
- 24h: commodity avg `0.3209` n `12`; crypto_alt avg `-4.6114` n `233`; crypto_major avg `-3.2637` n `8`; equity avg `-1.2793` n `134`; fx avg `0.0954` n `6`; index avg `-0.118` n `26`; metal avg `-0.4191` n `20`; unknown avg `-1.081` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
