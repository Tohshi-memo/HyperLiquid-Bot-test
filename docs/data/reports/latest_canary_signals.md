# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T03:22:28.033722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0097` n `12`; crypto_alt avg `-0.0394` n `233`; crypto_major avg `-0.0209` n `8`; equity avg `-0.057` n `134`; fx avg `0.0102` n `6`; index avg `-0.006` n `26`; metal avg `-0.019` n `20`; unknown avg `-0.1155` n `797`
- 1h: commodity avg `-0.0546` n `12`; crypto_alt avg `0.8706` n `233`; crypto_major avg `0.6146` n `8`; equity avg `0.1534` n `134`; fx avg `0.0198` n `6`; index avg `0.0368` n `26`; metal avg `0.0042` n `20`; unknown avg `121.5885` n `795`
- 4h: commodity avg `-0.2227` n `12`; crypto_alt avg `-0.0339` n `233`; crypto_major avg `0.3994` n `8`; equity avg `-0.2501` n `134`; fx avg `0.0158` n `6`; index avg `0.0124` n `26`; metal avg `-0.0132` n `20`; unknown avg `8.3636` n `789`
- 24h: commodity avg `-0.0876` n `12`; crypto_alt avg `-2.4759` n `233`; crypto_major avg `-1.4348` n `8`; equity avg `-1.2577` n `134`; fx avg `0.0236` n `6`; index avg `-0.2002` n `26`; metal avg `0.3895` n `20`; unknown avg `1.246` n `667`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
