# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T18:22:32.880584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.43` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `-1.7407` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.4986` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.062` n `12`; crypto_alt avg `-0.7852` n `228`; crypto_major avg `-0.426` n `8`; equity avg `0.0863` n `69`; fx avg `-0.0202` n `6`; index avg `0.0608` n `23`; metal avg `0.0099` n `18`; unknown avg `-0.2967` n `422`
- 1h: commodity avg `-0.0577` n `12`; crypto_alt avg `-0.6107` n `228`; crypto_major avg `-0.4559` n `8`; equity avg `-0.1792` n `69`; fx avg `-0.03` n `6`; index avg `-0.0395` n `23`; metal avg `-0.0542` n `18`; unknown avg `-0.4827` n `422`
- 4h: commodity avg `0.3377` n `12`; crypto_alt avg `-1.2661` n `228`; crypto_major avg `-1.3875` n `8`; equity avg `0.3532` n `69`; fx avg `-0.0262` n `6`; index avg `0.1111` n `23`; metal avg `0.0051` n `18`; unknown avg `-1.28` n `422`
- 24h: commodity avg `0.2105` n `12`; crypto_alt avg `-3.3669` n `228`; crypto_major avg `-3.6417` n `8`; equity avg `-0.0607` n `69`; fx avg `0.0448` n `6`; index avg `0.0028` n `23`; metal avg `0.1045` n `18`; unknown avg `-0.6452` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
