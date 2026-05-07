# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T10:37:01.818806+00:00`
- Correlation status: `ready`
- Asset price records: `542`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2422` n `12`; crypto_alt avg `-0.207` n `228`; crypto_major avg `-0.2393` n `8`; equity avg `-0.1677` n `65`; fx avg `-0.0072` n `4`; index avg `-0.0157` n `23`; metal avg `-0.0373` n `18`; unknown avg `-0.1015` n `366`
- 1h: commodity avg `0.4394` n `12`; crypto_alt avg `-0.3182` n `228`; crypto_major avg `-0.4153` n `8`; equity avg `-0.2968` n `65`; fx avg `0.0049` n `4`; index avg `-0.068` n `23`; metal avg `-0.0984` n `18`; unknown avg `-0.0046` n `358`
- 4h: commodity avg `-0.4926` n `12`; crypto_alt avg `0.0984` n `228`; crypto_major avg `-0.3573` n `8`; equity avg `0.0529` n `65`; fx avg `0.0298` n `4`; index avg `-0.0871` n `23`; metal avg `0.4949` n `18`; unknown avg `0.1797` n `358`
- 24h: commodity avg `-0.0956` n `7`; crypto_alt avg `-0.431` n `223`; crypto_major avg `-2.4789` n `7`; equity avg `0.1852` n `47`; fx avg `0.1877` n `4`; index avg `0.2053` n `6`; metal avg `0.936` n `7`; unknown avg `0.9474` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1309`, n `538`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1233`, n `538`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0955`, n `538`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0822`, n `534`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0821`, n `534`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0783`, n `534`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0781`, n `534`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0757`, n `534`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0721`, n `538`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `534`, weak_sample_signal
