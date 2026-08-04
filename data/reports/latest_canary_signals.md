# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T12:17:06.661447+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0306` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `-0.065` n `8`; equity avg `-0.0403` n `107`; fx avg `0.0218` n `6`; index avg `-0.0041` n `25`; metal avg `0.0391` n `20`; unknown avg `-0.0026` n `781`
- 1h: commodity avg `-0.5007` n `12`; crypto_alt avg `-0.056` n `230`; crypto_major avg `0.0522` n `8`; equity avg `0.0955` n `107`; fx avg `-0.0527` n `6`; index avg `0.0282` n `25`; metal avg `0.2419` n `20`; unknown avg `0.0249` n `781`
- 4h: commodity avg `-0.7639` n `12`; crypto_alt avg `-0.1254` n `230`; crypto_major avg `0.4656` n `8`; equity avg `0.4689` n `107`; fx avg `-0.081` n `6`; index avg `0.0852` n `25`; metal avg `0.3087` n `20`; unknown avg `0.1634` n `781`
- 24h: commodity avg `-0.4436` n `12`; crypto_alt avg `0.8815` n `230`; crypto_major avg `1.6522` n `8`; equity avg `5.2369` n `107`; fx avg `0.0418` n `6`; index avg `0.6272` n `25`; metal avg `0.7661` n `20`; unknown avg `0.8901` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
