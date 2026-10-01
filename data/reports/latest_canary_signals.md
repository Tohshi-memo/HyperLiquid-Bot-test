# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T16:52:32.345960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0507` n `13`; crypto_alt avg `-0.3064` n `234`; crypto_major avg `-0.1334` n `8`; equity avg `0.0392` n `142`; fx avg `-0.0216` n `6`; index avg `-0.0117` n `26`; metal avg `-0.0369` n `20`; unknown avg `0.0657` n `975`
- 1h: commodity avg `-0.2211` n `13`; crypto_alt avg `-0.3036` n `234`; crypto_major avg `-0.1837` n `8`; equity avg `0.3891` n `142`; fx avg `-0.0068` n `6`; index avg `0.0917` n `26`; metal avg `0.0287` n `20`; unknown avg `0.7294` n `967`
- 4h: commodity avg `-0.0695` n `13`; crypto_alt avg `-0.7554` n `234`; crypto_major avg `-0.5818` n `8`; equity avg `-0.1367` n `142`; fx avg `-0.1493` n `6`; index avg `-0.1411` n `26`; metal avg `-0.2686` n `20`; unknown avg `1.9748` n `909`
- 24h: commodity avg `-0.2828` n `13`; crypto_alt avg `-2.3355` n `234`; crypto_major avg `-1.3279` n `8`; equity avg `0.0883` n `142`; fx avg `-0.1178` n `6`; index avg `-0.0665` n `26`; metal avg `-0.1393` n `20`; unknown avg `0.0638` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
