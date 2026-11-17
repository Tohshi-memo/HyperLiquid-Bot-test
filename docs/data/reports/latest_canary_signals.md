# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T09:37:44.377381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1212` n `13`; crypto_alt avg `0.0657` n `239`; crypto_major avg `0.1859` n `8`; equity avg `0.0097` n `162`; fx avg `0.0064` n `6`; index avg `0.0101` n `27`; metal avg `-0.0043` n `20`; unknown avg `158.235` n `1266`
- 1h: commodity avg `0.1405` n `13`; crypto_alt avg `-0.4057` n `239`; crypto_major avg `-0.1783` n `8`; equity avg `-1.0217` n `162`; fx avg `-0.0262` n `6`; index avg `-0.0875` n `27`; metal avg `-0.0546` n `20`; unknown avg `18.6813` n `1260`
- 4h: commodity avg `0.3311` n `13`; crypto_alt avg `-0.975` n `239`; crypto_major avg `-0.993` n `8`; equity avg `-1.4214` n `162`; fx avg `-0.0476` n `6`; index avg `-0.1091` n `27`; metal avg `-0.274` n `20`; unknown avg `281.6069` n `1172`
- 24h: commodity avg `-0.6178` n `13`; crypto_alt avg `0.356` n `239`; crypto_major avg `0.9207` n `8`; equity avg `-3.4944` n `162`; fx avg `-0.0327` n `6`; index avg `-0.3825` n `27`; metal avg `-0.1179` n `20`; unknown avg `64.3394` n `1115`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1456`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
