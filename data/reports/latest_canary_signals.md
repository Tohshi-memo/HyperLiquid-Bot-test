# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T03:52:12.955168+00:00`
- Correlation status: `ready`
- Asset price records: `611`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0312` n `12`; crypto_alt avg `0.1667` n `228`; crypto_major avg `-0.0433` n `8`; equity avg `0.0023` n `65`; fx avg `0.0179` n `5`; index avg `-0.01` n `23`; metal avg `-0.102` n `18`; unknown avg `-0.0207` n `365`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `0.3264` n `228`; crypto_major avg `0.0024` n `8`; equity avg `0.0965` n `65`; fx avg `0.0225` n `5`; index avg `0.0197` n `23`; metal avg `0.1562` n `18`; unknown avg `-0.171` n `365`
- 4h: commodity avg `-0.4763` n `12`; crypto_alt avg `0.1068` n `228`; crypto_major avg `-0.3715` n `8`; equity avg `0.3744` n `65`; fx avg `0.1343` n `5`; index avg `0.2865` n `23`; metal avg `0.6283` n `18`; unknown avg `-0.1966` n `365`
- 24h: commodity avg `0.3546` n `12`; crypto_alt avg `2.5258` n `228`; crypto_major avg `-1.1404` n `8`; equity avg `-1.0014` n `65`; fx avg `0.1586` n `5`; index avg `-0.6085` n `23`; metal avg `0.4701` n `18`; unknown avg `0.0404` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1302`, n `607`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1197`, n `607`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1111`, n `607`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `607`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1093`, n `603`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1075`, n `603`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `603`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `603`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0791`, n `603`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `607`, weak_sample_signal
