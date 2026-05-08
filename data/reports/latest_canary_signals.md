# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T18:01:26.802884+00:00`
- Correlation status: `ready`
- Asset price records: `668`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2857` n `12`; crypto_alt avg `0.101` n `228`; crypto_major avg `0.0125` n `8`; equity avg `0.153` n `65`; fx avg `-0.0006` n `5`; index avg `0.1193` n `23`; metal avg `0.1752` n `18`; unknown avg `0.1972` n `375`
- 1h: commodity avg `-0.3261` n `12`; crypto_alt avg `0.6703` n `228`; crypto_major avg `0.7673` n `8`; equity avg `0.37` n `65`; fx avg `0.0019` n `5`; index avg `0.2561` n `23`; metal avg `0.3046` n `18`; unknown avg `0.1669` n `375`
- 4h: commodity avg `-0.1049` n `12`; crypto_alt avg `2.0694` n `228`; crypto_major avg `1.307` n `8`; equity avg `0.5364` n `65`; fx avg `0.0005` n `5`; index avg `0.3694` n `23`; metal avg `0.1228` n `18`; unknown avg `0.1222` n `375`
- 24h: commodity avg `0.3646` n `12`; crypto_alt avg `2.83` n `228`; crypto_major avg `0.7784` n `8`; equity avg `2.5808` n `65`; fx avg `0.1763` n `5`; index avg `1.3555` n `23`; metal avg `0.5415` n `18`; unknown avg `0.4208` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.121`, n `660`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1166`, n `660`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.111`, n `664`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0966`, n `660`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0962`, n `664`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0944`, n `660`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0706`, n `664`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `664`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0667`, n `664`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0659`, n `660`, weak_sample_signal
