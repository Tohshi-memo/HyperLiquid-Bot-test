# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T18:37:16.049973+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1222` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.3852` n `12`; crypto_alt avg `0.1717` n `228`; crypto_major avg `0.0976` n `8`; equity avg `0.3849` n `67`; fx avg `0.0022` n `6`; index avg `0.3624` n `23`; metal avg `0.0295` n `18`; unknown avg `-0.1111` n `396`
- 1h: commodity avg `-0.7479` n `12`; crypto_alt avg `1.0283` n `228`; crypto_major avg `0.876` n `8`; equity avg `0.5404` n `67`; fx avg `0.0019` n `6`; index avg `0.4177` n `23`; metal avg `0.0904` n `18`; unknown avg `1.0436` n `396`
- 4h: commodity avg `-0.5181` n `12`; crypto_alt avg `2.2694` n `228`; crypto_major avg `1.6041` n `8`; equity avg `0.9237` n `67`; fx avg `0.0062` n `6`; index avg `0.3139` n `23`; metal avg `0.2245` n `18`; unknown avg `2.025` n `396`
- 24h: commodity avg `-0.4597` n `12`; crypto_alt avg `-0.7153` n `228`; crypto_major avg `-0.4407` n `8`; equity avg `-0.0411` n `67`; fx avg `0.0104` n `6`; index avg `0.1931` n `23`; metal avg `-0.0691` n `18`; unknown avg `-1.6054` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
