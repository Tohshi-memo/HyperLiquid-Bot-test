# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T15:07:22.993431+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `0.1639` n `228`; crypto_major avg `0.1669` n `8`; equity avg `0.077` n `67`; fx avg `0.0186` n `6`; index avg `0.086` n `23`; metal avg `0.1154` n `18`; unknown avg `0.0404` n `386`
- 1h: commodity avg `-0.1971` n `12`; crypto_alt avg `-0.5105` n `228`; crypto_major avg `-0.4614` n `8`; equity avg `0.0553` n `67`; fx avg `0.0236` n `6`; index avg `0.1399` n `23`; metal avg `-0.0391` n `18`; unknown avg `-0.0046` n `386`
- 4h: commodity avg `-0.6583` n `12`; crypto_alt avg `-0.523` n `228`; crypto_major avg `-0.0861` n `8`; equity avg `0.1377` n `67`; fx avg `0.0078` n `6`; index avg `0.4248` n `23`; metal avg `-0.6324` n `18`; unknown avg `0.5759` n `386`
- 24h: commodity avg `-2.1925` n `12`; crypto_alt avg `1.6182` n `228`; crypto_major avg `0.0324` n `8`; equity avg `1.2825` n `67`; fx avg `0.1396` n `6`; index avg `1.373` n `23`; metal avg `0.2764` n `18`; unknown avg `0.6332` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0401`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0386`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0385`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0382`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0329`, n `668`, weak_sample_signal
