# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T07:37:25.667999+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `13`; crypto_alt avg `0.0793` n `235`; crypto_major avg `0.0459` n `8`; equity avg `-0.0225` n `150`; fx avg `0.005` n `6`; index avg `-0.0168` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.1414` n `1117`
- 1h: commodity avg `0.0013` n `13`; crypto_alt avg `-0.0823` n `235`; crypto_major avg `-0.0309` n `8`; equity avg `-0.0464` n `150`; fx avg `0.0007` n `6`; index avg `-0.0312` n `26`; metal avg `0.0019` n `20`; unknown avg `1.6452` n `1115`
- 4h: commodity avg `0.0382` n `13`; crypto_alt avg `0.1523` n `235`; crypto_major avg `0.2664` n `8`; equity avg `-0.0415` n `150`; fx avg `0.0067` n `6`; index avg `-0.0215` n `26`; metal avg `-0.0223` n `20`; unknown avg `0.2187` n `1092`
- 24h: commodity avg `0.0563` n `13`; crypto_alt avg `1.2423` n `235`; crypto_major avg `-0.122` n `8`; equity avg `-0.2248` n `150`; fx avg `-0.0533` n `6`; index avg `-0.0346` n `26`; metal avg `-0.0031` n `20`; unknown avg `666.8644` n `904`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.15`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
