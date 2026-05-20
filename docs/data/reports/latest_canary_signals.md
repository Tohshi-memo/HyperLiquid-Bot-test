# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T06:52:14.438616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.161` n `12`; crypto_alt avg `0.2247` n `228`; crypto_major avg `0.1906` n `8`; equity avg `0.0985` n `66`; fx avg `0.0004` n `6`; index avg `0.0527` n `23`; metal avg `0.3967` n `18`; unknown avg `0.06` n `384`
- 1h: commodity avg `-0.405` n `12`; crypto_alt avg `0.1919` n `228`; crypto_major avg `0.2862` n `8`; equity avg `0.3945` n `66`; fx avg `-0.0393` n `6`; index avg `0.1413` n `23`; metal avg `0.6109` n `18`; unknown avg `0.0984` n `374`
- 4h: commodity avg `-0.3839` n `12`; crypto_alt avg `1.3452` n `228`; crypto_major avg `1.0928` n `8`; equity avg `0.601` n `66`; fx avg `-0.004` n `6`; index avg `0.2537` n `23`; metal avg `1.057` n `18`; unknown avg `0.348` n `374`
- 24h: commodity avg `-0.0379` n `12`; crypto_alt avg `-0.1573` n `228`; crypto_major avg `0.0399` n `8`; equity avg `0.4074` n `66`; fx avg `-0.1519` n `6`; index avg `-0.455` n `23`; metal avg `-1.2234` n `18`; unknown avg `0.0711` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0513`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0469`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0441`, n `668`, weak_sample_signal
