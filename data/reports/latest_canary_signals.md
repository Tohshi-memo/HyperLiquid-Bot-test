# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T11:37:35.031725+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `13`; crypto_alt avg `0.4892` n `239`; crypto_major avg `0.5995` n `8`; equity avg `0.1827` n `166`; fx avg `0.0117` n `6`; index avg `0.0188` n `27`; metal avg `0.009` n `20`; unknown avg `2.4753` n `1242`
- 1h: commodity avg `0.0129` n `13`; crypto_alt avg `0.5508` n `239`; crypto_major avg `0.8576` n `8`; equity avg `0.2928` n `166`; fx avg `0.027` n `6`; index avg `0.0246` n `27`; metal avg `0.003` n `20`; unknown avg `1.726` n `1236`
- 4h: commodity avg `0.0014` n `13`; crypto_alt avg `0.3924` n `239`; crypto_major avg `0.5` n `8`; equity avg `0.0721` n `166`; fx avg `0.0583` n `6`; index avg `0.0086` n `27`; metal avg `0.0436` n `20`; unknown avg `2.025` n `1218`
- 24h: commodity avg `0.4952` n `13`; crypto_alt avg `-4.7988` n `239`; crypto_major avg `-5.3065` n `8`; equity avg `-4.1595` n `166`; fx avg `-0.0821` n `6`; index avg `-0.4505` n `27`; metal avg `-0.4476` n `20`; unknown avg `-0.4945` n `1145`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
