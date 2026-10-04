# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T20:22:27.166500+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `13`; crypto_alt avg `0.0787` n `235`; crypto_major avg `0.1129` n `8`; equity avg `0.0173` n `144`; fx avg `0.0016` n `6`; index avg `0.0032` n `26`; metal avg `0.0042` n `20`; unknown avg `0.1346` n `1078`
- 1h: commodity avg `0.0007` n `13`; crypto_alt avg `0.0188` n `235`; crypto_major avg `-0.0225` n `8`; equity avg `0.0382` n `144`; fx avg `0.0002` n `6`; index avg `0.0043` n `26`; metal avg `0.0` n `20`; unknown avg `0.239` n `1064`
- 4h: commodity avg `0.092` n `13`; crypto_alt avg `0.4759` n `235`; crypto_major avg `0.3348` n `8`; equity avg `0.0532` n `144`; fx avg `-0.0063` n `6`; index avg `0.0098` n `26`; metal avg `0.0112` n `20`; unknown avg `0.4265` n `1064`
- 24h: commodity avg `0.0258` n `13`; crypto_alt avg `0.9555` n `235`; crypto_major avg `0.9358` n `8`; equity avg `0.1852` n `144`; fx avg `0.0147` n `6`; index avg `-0.0153` n `26`; metal avg `0.0053` n `20`; unknown avg `0.4726` n `1020`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1844`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1777`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
