# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T04:37:28.296790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0673` n `13`; crypto_alt avg `-0.0941` n `239`; crypto_major avg `-0.0685` n `8`; equity avg `0.0419` n `162`; fx avg `-0.0057` n `6`; index avg `0.0145` n `27`; metal avg `0.0099` n `20`; unknown avg `-0.2241` n `1264`
- 1h: commodity avg `-0.0295` n `13`; crypto_alt avg `-0.2573` n `239`; crypto_major avg `-0.1559` n `8`; equity avg `-0.7128` n `162`; fx avg `-0.0321` n `6`; index avg `-0.0805` n `27`; metal avg `-0.0454` n `20`; unknown avg `201.9453` n `1250`
- 4h: commodity avg `-0.1758` n `13`; crypto_alt avg `0.952` n `239`; crypto_major avg `0.9801` n `8`; equity avg `0.5275` n `162`; fx avg `0.0041` n `6`; index avg `0.0245` n `27`; metal avg `0.1852` n `20`; unknown avg `0.2165` n `1246`
- 24h: commodity avg `-1.1207` n `13`; crypto_alt avg `0.4099` n `239`; crypto_major avg `0.9965` n `8`; equity avg `-2.6964` n `162`; fx avg `-0.0724` n `6`; index avg `-0.2813` n `27`; metal avg `-0.0876` n `20`; unknown avg `561.0813` n `987`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
