# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T11:52:18.689876+00:00`
- Correlation status: `ready`
- Asset price records: `643`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0232` n `12`; crypto_alt avg `0.0819` n `228`; crypto_major avg `0.1045` n `8`; equity avg `0.056` n `65`; fx avg `-0.0001` n `5`; index avg `0.0562` n `23`; metal avg `-0.1104` n `18`; unknown avg `-0.0053` n `375`
- 1h: commodity avg `-0.0556` n `12`; crypto_alt avg `0.0536` n `228`; crypto_major avg `0.0156` n `8`; equity avg `0.0678` n `65`; fx avg `0.01` n `5`; index avg `0.1681` n `23`; metal avg `-0.1` n `18`; unknown avg `-0.0498` n `375`
- 4h: commodity avg `-0.0077` n `12`; crypto_alt avg `0.7439` n `228`; crypto_major avg `0.5068` n `8`; equity avg `0.4759` n `65`; fx avg `0.044` n `5`; index avg `0.2246` n `23`; metal avg `0.2343` n `18`; unknown avg `0.4313` n `375`
- 24h: commodity avg `1.5511` n `12`; crypto_alt avg `1.2946` n `228`; crypto_major avg `-1.1432` n `8`; equity avg `-0.3327` n `65`; fx avg `0.2566` n `5`; index avg `-0.3338` n `23`; metal avg `-0.6768` n `18`; unknown avg `-0.2582` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1344`, n `635`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1343`, n `635`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1071`, n `639`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `639`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0915`, n `639`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `639`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0884`, n `635`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0824`, n `635`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.078`, n `635`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `639`, weak_sample_signal
