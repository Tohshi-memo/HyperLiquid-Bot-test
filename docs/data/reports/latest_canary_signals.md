# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T00:52:29.993058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `13`; crypto_alt avg `0.085` n `239`; crypto_major avg `0.0147` n `8`; equity avg `0.0835` n `158`; fx avg `-0.0014` n `6`; index avg `0.0023` n `27`; metal avg `0.005` n `20`; unknown avg `0.5823` n `1261`
- 1h: commodity avg `-0.0142` n `13`; crypto_alt avg `0.2078` n `239`; crypto_major avg `0.0262` n `8`; equity avg `0.0719` n `158`; fx avg `-0.0208` n `6`; index avg `-0.0002` n `27`; metal avg `0.0086` n `20`; unknown avg `0.0771` n `1249`
- 4h: commodity avg `0.0433` n `13`; crypto_alt avg `-0.0266` n `239`; crypto_major avg `0.2172` n `8`; equity avg `0.2594` n `158`; fx avg `0.0018` n `6`; index avg `0.0166` n `27`; metal avg `0.0435` n `20`; unknown avg `-0.564` n `1173`
- 24h: commodity avg `0.1155` n `13`; crypto_alt avg `1.108` n `239`; crypto_major avg `-0.2893` n `8`; equity avg `1.8587` n `158`; fx avg `-0.1015` n `6`; index avg `0.2996` n `27`; metal avg `-0.0425` n `20`; unknown avg `8.3353` n `1022`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
