# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-19T16:07:20.359844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0382` n `12`; crypto_alt avg `-0.053` n `228`; crypto_major avg `-0.0732` n `8`; equity avg `0.0799` n `66`; fx avg `-0.0122` n `6`; index avg `0.0315` n `23`; metal avg `0.1111` n `18`; unknown avg `-0.1364` n `383`
- 1h: commodity avg `0.0858` n `12`; crypto_alt avg `-0.0959` n `228`; crypto_major avg `0.0044` n `8`; equity avg `0.6295` n `66`; fx avg `-0.0084` n `6`; index avg `0.3532` n `23`; metal avg `0.3172` n `18`; unknown avg `0.0207` n `383`
- 4h: commodity avg `0.2454` n `12`; crypto_alt avg `-0.3705` n `228`; crypto_major avg `-0.1617` n `8`; equity avg `0.3167` n `66`; fx avg `-0.0339` n `6`; index avg `-0.2442` n `23`; metal avg `-1.1093` n `18`; unknown avg `-0.165` n `383`
- 24h: commodity avg `0.6066` n `12`; crypto_alt avg `0.5469` n `228`; crypto_major avg `0.8764` n `8`; equity avg `-0.1958` n `66`; fx avg `0.0353` n `6`; index avg `-0.7061` n `23`; metal avg `-1.8407` n `18`; unknown avg `0.0296` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
