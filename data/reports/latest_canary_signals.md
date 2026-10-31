# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T20:37:31.995939+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `-0.1266` n `238`; crypto_major avg `-0.0972` n `8`; equity avg `-0.0049` n `156`; fx avg `-0.0009` n `6`; index avg `0.0011` n `27`; metal avg `-0.0044` n `20`; unknown avg `0.2737` n `1236`
- 1h: commodity avg `-0.0241` n `13`; crypto_alt avg `-0.3225` n `238`; crypto_major avg `-0.1653` n `8`; equity avg `-0.0413` n `156`; fx avg `0.0155` n `6`; index avg `-0.0078` n `27`; metal avg `-0.0025` n `20`; unknown avg `0.4608` n `1200`
- 4h: commodity avg `0.0066` n `13`; crypto_alt avg `-0.9064` n `238`; crypto_major avg `-0.0977` n `8`; equity avg `0.0341` n `156`; fx avg `0.0018` n `6`; index avg `0.0002` n `27`; metal avg `-0.0152` n `20`; unknown avg `-0.2635` n `1164`
- 24h: commodity avg `-0.1523` n `13`; crypto_alt avg `0.5728` n `238`; crypto_major avg `0.0938` n `8`; equity avg `0.2201` n `156`; fx avg `-0.0107` n `6`; index avg `-0.03` n `27`; metal avg `0.0983` n `20`; unknown avg `0.9678` n `1073`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1457`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
