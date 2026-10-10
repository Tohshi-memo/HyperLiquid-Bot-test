# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T11:22:31.096567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `13`; crypto_alt avg `0.0572` n `235`; crypto_major avg `-0.0368` n `8`; equity avg `0.0018` n `150`; fx avg `-0.0076` n `6`; index avg `-0.0053` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.0114` n `1117`
- 1h: commodity avg `0.0002` n `13`; crypto_alt avg `0.1057` n `235`; crypto_major avg `-0.0565` n `8`; equity avg `0.0179` n `150`; fx avg `0.0043` n `6`; index avg `-0.0047` n `26`; metal avg `0.0031` n `20`; unknown avg `0.0986` n `1115`
- 4h: commodity avg `-0.2415` n `13`; crypto_alt avg `-0.1606` n `235`; crypto_major avg `-0.1265` n `8`; equity avg `-0.0259` n `150`; fx avg `-0.0012` n `6`; index avg `-0.0098` n `26`; metal avg `0.0003` n `20`; unknown avg `0.2706` n `1099`
- 24h: commodity avg `-0.121` n `13`; crypto_alt avg `1.9022` n `235`; crypto_major avg `0.2475` n `8`; equity avg `-0.2079` n `150`; fx avg `0.01` n `6`; index avg `-0.0122` n `26`; metal avg `0.0318` n `20`; unknown avg `631.8119` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1234`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
