# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T14:37:31.783348+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `-0.0686` n `228`; crypto_major avg `0.0613` n `8`; equity avg `0.0567` n `74`; fx avg `-0.0021` n `6`; index avg `0.0057` n `23`; metal avg `-0.1053` n `18`; unknown avg `0.0046` n `644`
- 1h: commodity avg `0.1175` n `12`; crypto_alt avg `-0.1121` n `228`; crypto_major avg `0.1536` n `8`; equity avg `-0.0157` n `74`; fx avg `-0.0111` n `6`; index avg `-0.0507` n `23`; metal avg `-0.1189` n `18`; unknown avg `-0.0294` n `644`
- 4h: commodity avg `-0.1037` n `12`; crypto_alt avg `0.3696` n `228`; crypto_major avg `0.9983` n `8`; equity avg `0.1716` n `74`; fx avg `0.0028` n `6`; index avg `0.2669` n `23`; metal avg `0.1681` n `18`; unknown avg `0.297` n `644`
- 24h: commodity avg `-1.0885` n `12`; crypto_alt avg `0.9301` n `228`; crypto_major avg `-0.0644` n `8`; equity avg `-0.1189` n `74`; fx avg `0.0122` n `6`; index avg `0.784` n `23`; metal avg `1.1285` n `18`; unknown avg `0.2316` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.053`, n `668`, weak_sample_signal
