# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T04:22:27.189991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `13`; crypto_alt avg `0.436` n `234`; crypto_major avg `0.4453` n `8`; equity avg `0.0406` n `142`; fx avg `-0.0013` n `6`; index avg `0.0007` n `26`; metal avg `0.0231` n `20`; unknown avg `1.0154` n `985`
- 1h: commodity avg `-0.0153` n `13`; crypto_alt avg `0.4631` n `234`; crypto_major avg `0.7353` n `8`; equity avg `0.0195` n `142`; fx avg `-0.0048` n `6`; index avg `0.0106` n `26`; metal avg `0.1074` n `20`; unknown avg `1.0476` n `977`
- 4h: commodity avg `-0.1852` n `13`; crypto_alt avg `0.6848` n `234`; crypto_major avg `1.1825` n `8`; equity avg `-0.041` n `142`; fx avg `-0.0702` n `6`; index avg `0.0142` n `26`; metal avg `0.1044` n `20`; unknown avg `2.6238` n `977`
- 24h: commodity avg `0.6208` n `13`; crypto_alt avg `-0.2257` n `234`; crypto_major avg `1.1314` n `8`; equity avg `0.4843` n `142`; fx avg `-0.2106` n `6`; index avg `0.0456` n `26`; metal avg `-0.0197` n `20`; unknown avg `0.5086` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1342`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
